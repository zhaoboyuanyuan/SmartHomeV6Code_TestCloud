# SmartHomeV6Code_TestCloud
物联云接口测试，api,sso，ent等接口

关于签名
       每个app会分配一个partnerId和partnerKey
       签名规则：
              partnerId+"&"+参数部分+"&"+partnerKey+"&"+当前时间戳(毫秒) 
              上述字符串进行sha1加密然后转换成小写字符串,就是本次请求的签名
       对于GET请求
              参数部分为：所有参数按照参数名升序排序，通过"&"拼接起来              
       对于POST请求
              参数部分为：request的body   
