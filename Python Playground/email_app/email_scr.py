import imapclient, pyzmail

class email_scr:   

    def __init__(self):
        self.Client_Name = ""
        self.Order_No = 0
        self.Order_info = []
        self.Order_Details = ""
        self.Customer_email = ""
        self.Shipping_Details = ""
        self.Delivery_Meth = ""

    def toString(self):
        return str(
            "Client Name: " + self.Client_Name + "\n"
            "Order Number: " + str(self.Order_No) + "\n"
            "Order Details: " + self.Order_Details + "\n" 
            "Shipping Number: " + str(self.Shipping_No) + "\n"
            "Shipping Details: " + self.Shipping_Details)

    def totup(self): 
        email_tup = {self.Client_Name, self.Order_No, self.Order_Details, self.Shipping_No, self.Shipping_Details}
        return email_tup

    def parse_email(self, text_message):
        for i in text_message:
            if i == 'ORDER INFORMATION\r':
                self.Order_info.append(text_message[i:i+15])
            elif i == 'Order #:':
                self.Order_No = i+1


    def login(self,email_val):
        email_reader = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        email_reader.login( "admin@nah.com" , "nmope")

        email_reader.select_folder('INBOX', readonly=True)
        
        
        UIDs = email_reader.search(['SINCE','24-Apr-2020'])
        rawMessages = email_reader.fetch(UIDs, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(rawMessages[UIDs[email_val]][b'BODY[]'])
        if message.get_subject() == 'NICE! YOU JUST GOT AN ORDER':
            message_text = message.text_part.get_payload().decode(message.text_part.charset)
            text_list = message_text.split('\n')
            print(text_list)
            return parse_email(text_list)

        else:
            return 'done'
