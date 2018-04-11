import time
from itertools import repeat
from random import randint
import requests
from orderCreatePkg import DefaultProperties as dp

timeStamp = time.strftime("%d%m%y%H%M%S")
orderNo = open(timeStamp, "w")

for i in repeat(None, dp.no_of_orders):
  orderID = time.strftime("%#d%m%y") + str(randint(10, 99))
  payload = ('{ "id": '+ str(orderID) +', "shippingCharge": 0.0, "giftCharge": 0.0, "amountDue": 13000.0, "receiverName": "Mayukh Ghosh", "address": "&#x23;320,Myntra.com", "city": "Pune", "locality": "Vimanagar", "state": "MH", "zipcode": "4110114", "country": "INDIA", "mobile": "1234567898", "warehouse": "PTY", "cancellationReason": null, "onHold": false, "orderDate": "2017-06-01 05:15:58", "shippingMethod": "NORMAL", "expectedDeliveryTime": "2017-06-02 21:45:00", "processingStartTime": "2017-06-01 08:30:58", "processingCutoffTime": "2017-06-01 16:05:17", "courierCode": "ML", "paymentMethod": "cod", "senderName": null, "senderEmail": null, "receiverEmail": null, "sellerId": null, "giftMessage": null, "orderLineEntries": [{ "orderId": '+ str(orderID) +', "sku": "3787-10002218", "totalQuantity": 1, "cancelledQuantity": null, "mrp": 13000.0, "totalSellerDiscount": 0.0, "totalMarketplaceDiscount": 0.0, "totalPaymentReceived": 13000.0, "cancellationReason": null, "unitTaxAmount": null, "taxRate": null, "taxType": null, "orderLineId": null, "quantity": null, "customizedMessage": null }] }')

  url = dp.url+orderID

  s = requests.Session()
  s.headers.update({'Content-Type': 'application/json'})

  r = s.post(url , data=payload, auth=(dp.userName, dp.pwd))

  print(orderID)
  orderNo.write(orderID)
  orderNo.write('\n')
  print(r.json())

orderNo.close()
