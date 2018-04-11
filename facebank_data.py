# -*- coding: utf-8 -*-

instalmentBorrow_return=\
"""{
"respCode": "000003",
"respDesc": "处理中",
"sign": "ec2241ba62834e6b9b3460eb0476a26b",
"data":{
"merchantCode": "2000000000000001",
"targetCode": "31801032900510",
"userId": "bf0fcefe3cd9483ca17fa8872c38b9b8",
"status": "2"
}
}"""

queryInstalmentTarget_return=\
"""{"respCode":"000000","respDesc":"成功","sign":"0cf3e7fbd5b797dc67be24cf05a4c412","data":{"merchantCode":"2000000000000001","targetCode":"31801032900510","status":"4","transferStatus":"2","finishTime":"2018-03-30 02:12:02","raiseTotalAmt":"600000","receiveAmt":"600000","fee":"0","userId":"bb1417a4bd9649c4b9b61cd7eb097d09","loanUsage":"消费分期","repayType":"2","raiseEndTime":"2018-03-30 01:58:23","applyTime":"2018-03-30 01:08:23","feeType":"5","instalmentNum":3,"instalmentUnit":1,"cashDeposit":"0"}}"""

personalRegisterSendSms_return=\
"""{
    "status":true,
    "message":"应答状态码信息",
    "result":{
        "request_no"："请求流水号",
        "phone_token":"令牌信息"
        "resp_code":"响应码0000代表业务成功，其他业务失败",
        "resp_message":"响应信息描述"
    }
  }"""