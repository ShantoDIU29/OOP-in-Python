def call():
  print('caling someone i dont know')
  return 'call done'
class phone:
  price=4000
  color='brand'
  brand='samsung'
  feature=['camera','speaker','hammer']
  def call(self):
    print("calling one person")
  def send_sms(self,phone,sms):
    text=f'sending sms to{phone}and message{sms}'
    return text
  
my_phone=phone()
print(my_phone.feature)
my_phone.call() 
result=my_phone.send_sms(724355967,'hello how are you?')
print(result)