#! /usr/bin/env python3

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse

if __name__ == "__main__":

    rospy.init_node("turtle_spawn")
    # 创建服务客户端
    client = rospy.ServiceProxy("/spawn",Spawn)
    # 等待服务启动
    client.wait_for_service()
    # 创建请求数据
    req = SpawnRequest()
    req.x = 1.0
    req.y = 1.0
    req.theta = 3.14
    req.name = "turtle2"
    # 发送请求并处理响应
    try:
        response = client.call(req)
        rospy.loginfo("乌龟创建成功，名字是:%s",response.name)
    except Exception as e:
        rospy.loginfo(e)
