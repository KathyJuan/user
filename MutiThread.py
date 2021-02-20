import requests
import random
import json
import threading
import multiprocessing

prefixlist=['fgm','mik','b2b','had']
ordertypelist = [1,2,3,4,5]
channellist=[1,2,3,4]
useridlist=[1011,2011,3011,4011,5011,6011,7011,8011,9011,10011,11011,12011]
storyidlist=[1092,2092,3092,4092,5092,6092,7092,8092,9092,10092,11092,12092]
itemstatuslist=[1000,1500,2000,3000,3500,3600,3700,4000,7000,8000,8500,8600,8700,9000,9100,10000,11000,12000,13000,18000,19000,19100,20000]
createtimelist=[1612821966,1610143566,1612044366,1609365966,1606773966,1604095566,1601503566,1598825166,1596146766,1593554766,1590876366,1559253966,1577743566]
skunumberlist=['10371038','10643086','10643279','10644191','10644193','10644195','10644197','10644199','10644203','10644205','10645499']
parentOrganizationIdlist=['1111','2222','3333','4444','5555']
organizationIdlist=['11','22','33','44']




def createdate(count):
    for i in range(10000):
        print(count)
        print(i)
        parentOrderNumber = random.choice(prefixlist) + str(count)
        print(parentOrderNumber)
        channel = random.choice(channellist)
        ordertype = random.choice(ordertypelist)
        userid = random.choice(useridlist)
        storyid = random.choice(storyidlist)
        itemstatus = random.choice(itemstatuslist)
        createtime = random.choice(createtimelist)
        skunumber = random.choice(skunumberlist)
        organizationId = random.choice(organizationIdlist)
        parentOrganizationId = random.choice(parentOrganizationIdlist)
        headers = {
            'Connection': 'keep-alive',
            'content-type': 'application/json;charset=UTF-8',
            'Accept': 'application/json'
        }
        url = "http://localhost:8080/order/create"
        data0 = {
            "parentOrderNumber": str(parentOrderNumber),
            "userId": userid,
            "parentOrganizationId": str(parentOrganizationId),
            "organizationId": str(organizationId),
            "payments": [
                {
                    "paymentTransactionId": str(count),
                    "transactionType": 0,
                    "requestToken":"abcd",
                    "requestAmount": "98.0",
                    "creditLastFourDigit": "1233",
                    "rewardsId": "rewards001"
                }
            ],
            "billingAddress": {
                "address1": "address1",
                "city": "city1",
                "state": "state1",
                "zipCode": "55415",
                "firstName": "Daren",
                "lastName": "Xu",
                "phone": "13500000000"
            },
            "suborders": [
                {
                    "orderNumber": str(parentOrderNumber),
                    "orderPickupArrayIndex": 0,
                    "channel": channel,
                    "userId": userid,
                    "firstName": "Daren",
                    "lastName": "Xu",
                    "storeId": storyid,
                    "estimatedTax": "1.0",
                    "itemsSubtotal": "100.0",
                    "shippingHandlingCharge": "5.0",
                    "toManhattan": True,
                    "grandTotalCollected": "6.0",
                    "totalDiscount": "2.0",
                    "customerEmail": "DarenXu@test.com",
                    "orderType": ordertype,
                    "orderLine": [
                        {
                            "skuNumber": str(skunumber),
                            "orderLineShipmentArrayIndex": 0,
                            "itemType": 0,
                            "quantity": 1,
                            "thumbnail": "string",
                            "productName": "productName",
                            "rating": 0,
                            "price": "1.1",
                            "itemSubtotal": "1.1",
                            "estimatedTax": "1.1",
                            "totalDiscount": "1.1",
                            "taxRate": "1.1",
                            "refundDeadline": str(createtime),
                            "returnDeadline": str(createtime),
                            "hazmat": True
                        }
                    ],
                    "pickups": [
                        {
                            "shipToLocationId": "20",
                            "promiseReadyDate": str(createtime),
                            "pickupDeadlineTime": str(createtime),
                            "pickupPersonFirstname": "Daren",
                            "pickupPersonLastname": "Xu",
                            "pickupPersonEmail": "DarenXu@test.com",
                            "pickupPersonPhone": "13500000000",
                            "orderPickupType": 1,
                            "address1": "add001",
                            "city": "city001",
                            "state": "state001",
                            "countryCode": "US",
                            "zipCode": "55000"
                        }
                    ],
                    "shipments": [
                        {
                            "address1": "add001",
                            "city": "city001",
                            "state": "state001",
                            "zipCode": "55000",
                            "firstName": "juan",
                            "lastName": "han",
                            "orderShipmentType": 1
                        }
                    ]
                }
            ]
        }
        data1=json.dumps(data0)
        print(data1)
        req1 = requests.post(url=url, data=data1, headers=headers)
        print(req1.status_code)
        print(req1.text)
        count = count + 1
        print(count)


if __name__=="__main__":
    threads = []
    for j in range(5000):
        countinit = 4200000000 + j * 100000
        t1 = threading.Thread(target=createdate, args=(countinit,))
        threads.append(t1)
        print(threads)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

    print("teste")