import requests

# 微信文章链接
weixin_article_url = "https://mp.weixin.qq.com/s/v6DK29ZJ5ZwD_Mp4ZtSoBg"

# API接口地址
api_url = "https://api.pearktrue.cn/api/wx/wzsp.php"

# 请求参数
params = {
    "url": weixin_article_url
}

# 发送GET请求
response = requests.get(api_url, params=params)

# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON响应内容
    result = response.json()
    
    # 检查状态码
    if result.get("code") == 200:
        # 打印获取到的视频信息
        print("文章标题:", result.get("title"))
        print("文章作者:", result.get("author"))
        print("获取到的视频数量:", result.get("count"))
        
        # 遍历视频数据
        for video_info in result.get("data", []):
            for video_data in video_info.get("video_data", []):
                print("视频清晰度:", video_data.get("clarity"))
                print("视频大小:", video_data.get("format_size"))
                print("视频URL:", video_data.get("video_url"))
                print()
    else:
        print("发生错误:", result.get("msg"))
else:
    print("请求失败，状态码:", response.status_code)