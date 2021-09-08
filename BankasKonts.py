from os import system, name 

class Bank:
  __bank_name: str
  __location: int

  def __init__(self, bank_name, location):
    self.__bank_name = bank_name
    self.__location = location
    
  def get_bank_name(self):
    return self.__bank_name

  def get_location(self):
    return self.__location

  def set_bank_name(self, bank_name):
    self.__bank_name = bank_name

  def set_location(self, location):
    self.__location = location

class Client(Bank):
  __client_name: str
  __id: str
  __account_balance: float
  __password: str
  __currency: str
  __password_tries: int

  def __init__(self, client_name, id, account_balance, password, bank_name, location):
      self.__client_name = client_name
      self.__id = id
      self.__account_balance = account_balance
      self.__password = password
      self.__currency = "EUR"
      self.__password_tries = 0
      super().__init__(bank_name, location)

  def get_client_name(self):
    return self.__client_name

  def get_id(self):
    return self.__id

  def get_account_balance(self):
    return self.__account_balance

  def get_password(self):
    return self.__password

  def get_currency(self):
    return self.__currency

  def get_password_tries(self):
    return self.__password_tries

  def set_client_name(self, client_name):
    self.__client_name = client_name

  def set_id(self, id):
    self.__id = id

  def set_account_balance(self, account_balance):
    self.__account_balance = account_balance

  def set_password(self, password):
    self.__password = password
  
  def set_currency(self, currency):
    self.__currency = currency

  def set_password_tries(self, password_tries):
    self.__password_tries = password_tries
  
  def add_password_try(self):
    self.__password_tries += 1

  def add_balance(self, balance):
    self.__account_balance += balance

  def reduce_balance(self, balance):
    self.__account_balance -= balance

  def change_currency(self, current_cur, new_cur, cur_name):
    self.__account_balance = (self.__account_balance / current_cur) * new_cur
    self.__currency = cur_name

def clear(): 
  if name == 'nt': 
    _ = system('cls') 
  else: 
    _ = system('clear')

def validate_choice(choice, min_value, max_value):
  if choice.isdigit():
    choice = int(choice)
    if choice >= min_value and choice <= max_value:
      return 1
    else:
      clear()
      print("No option found")
      return 0
  else:
    clear()
    print("No option found")
    return 0

bank_list = []
client_list = []
currency = ["EUR", "USD", "GBP", "JPY"]
currency_value = [1, 1.19, 0.89, 123.35]

bank_list.append(Bank("Swedbank", "Sweden"))
bank_list.append(Bank("Citadele", "Latvia"))

while True:
  option = 0
  validate = 0 
  while validate == 0:
    print("Login as:")
    option = input("1. Bank\n2. Client\n\n0. Exit\n")
    validate = validate_choice(option, 0, 2)
  option = int(option)
  clear()

  if option == 1:  #bank option
    validate = 0
    while validate == 0:
      print("Choose bank:")
      for bank in range(len(bank_list)):
        print(str(bank + 1) + ".", bank_list[bank].get_bank_name())
      bank_number = input()
      validate = validate_choice(bank_number, 1, len(bank_list))
    bank_number = int(bank_number)
    clear()

    while True:
      validate = 0
      while validate == 0:
        print("Current bank:", bank_list[bank_number - 1].get_bank_name())
        option = input("1. Add client\n2. Show clients\n3. Search client\n\n0. Back\n")
        validate = validate_choice(option, 0, 3)
      option = int(option)
      clear()

      if option == 1:  #add client
        bank_name = bank_list[bank_number - 1].get_bank_name()
        location = bank_list[bank_number - 1].get_location()
        client_name = input("Clients name: ")
        
        check_id = 0
        while check_id == 0 or check_id == 1:
          check_id = 0
          client_id = input("Clients id: ")
          for client in client_list:
            if client_id == client.get_id():
              print("ID already exists")
              check_id = 1
          if check_id == 0:
            break
          
        while True:
          value = input("Account balance: ")
          try:
            account_balance = int(value)
            break
          except ValueError:
            try:
              account_balance = float(value)
              break
            except ValueError:
              print("Must be a number")

        while True:
          password = input("Password: ")
          if len(password) <= 3:
            print("Password must be longer than 3 symbols")
          else: 
            break

        client_list.append(Client(client_name, client_id, account_balance, password, bank_name, location))
        clear()

      elif option == 2:  #show all clients
        no_clients = 1
        for client in client_list:
          if client.get_bank_name() == bank_list[bank_number - 1].get_bank_name():
            print("Bank:", client.get_bank_name(), "\nClients name:", client.get_client_name(), "\nClients id:", client.get_id(), "\nAccount balance:", "%0.2f" % client.get_account_balance(), client.get_currency(), "\nPassword:", client.get_password(), "\n")
            no_clients = 0
        input("Press Enter to continue ")
        clear()

        if no_clients == 1:
          print("No clients found")
          input("\nPress Enter to continue ")
          clear()
      
      elif option == 3:  #search client
        not_found = 1
        search = input("Enter clients name: ")
        for client in client_list:
          if client.get_bank_name() == bank_list[bank_number - 1].get_bank_name():
            if client.get_client_name() == search:
              print("Name:", client.get_client_name(), "\nClients id:", client.get_id(), "\nAccount balance:", "%0.2f" % client.get_account_balance(), client.get_currency(), "\nPassword:", client.get_password())
              not_found = 0
        input("\nPress Enter to continue ")
        clear()

        if not_found == 1:
            print("Client not found")
            input("\nPress Enter to continue ")
            clear()
            

      elif option == 0:
        break
  
  elif option == 2:  #client option
    back = 1
    while True:
      if back == 0:
        break
      print("Type 0 to go back")
      client_id = input("Enter ID: ")
      clear()
      if client_id == "0":
        break

      else:
        not_found = 1
        for client in client_list:
          if client.get_id() == client_id:
            if client.get_password_tries() == 3:
              print("Account blocked\n")

            else:
              while client.get_password_tries() < 3:
                if back == 0:
                  break
                print("Type 0 to go back")
                password = input("Enter password: ")
                clear()
                if password == "0":
                  break

                elif client.get_password() == password:  #correct password
                  client.set_password_tries(0)
                  while True:
                    validate = 0
                    while validate == 0:
                      print("Bank:", client.get_bank_name(), "\nName:", client.get_client_name())
                      option = input("1. Account balance\n2. Change data\n\n0. Back\n")
                      validate = validate_choice(option, 0, 2)
                    option = int(option)
                    clear()

                    if option == 1:  #account balance
                      while True:
                        validate = 0
                        while validate == 0:
                          print("Account balance:", "%0.2f" % client.get_account_balance(), client.get_currency())
                          option = input("1. Add balance\n2. Reduce balance\n3. Change currency\n\n0. Back\n")
                          validate = validate_choice(option, 0, 3)
                        option = int(option)
                        clear()

                        if option == 1:  #add balance
                          while True:
                            value = input("Amount to add: ")
                            try:
                              money = int(value)
                              if money <= 0:
                                clear()
                                print("Must be a number bigger than 0")
                                continue
                              else:
                                break
                            except ValueError:
                              try:
                                money = float(value)
                                if money <= 0:
                                  clear()
                                  print("Must be a number bigger than 0")
                                  continue
                                else:
                                  break
                              except ValueError:
                                clear()
                                print("Must be a number bigger than 0")
                          client.add_balance(money)
                          print("New account balance:", "%0.2f" % client.get_account_balance(), client.get_currency())
                          clear()

                        elif option == 2: #reduce balance
                          while True:
                            value = input("Amount to add: ")
                            try:
                              money = int(value)
                              if money <= 0:
                                clear()
                                print("Must be a number bigger than 0")
                                continue
                              else:
                                break
                            except ValueError:
                              try:
                                money = float(value)
                                if money <= 0:
                                  clear()
                                  print("Must be a number bigger than 0")
                                  continue
                                else:
                                  break
                              except ValueError:
                                clear()
                                print("Must be a number bigger than 0")
                          client.reduce_balance(money)
                          print("New account balance:", "%0.2f" % client.get_account_balance(), client.get_currency())
                          clear()

                        elif option == 3:  #change currency
                          while True:
                            validate = 0
                            while validate == 0:
                              print("Change currency to:")
                              for cur in range(len(currency)):
                                print(str(cur + 1) + ".", currency[cur])
                              option = input("\n0. Back\n")
                              validate = validate_choice(option, 0, 4)
                            option = int(option)
                            clear()

                            if option == 0:  #back
                              break

                            elif option >= 1 and option <= 4:  #choose currency
                              current_cur = currency.index(client.get_currency())
                              client.change_currency(currency_value[current_cur], currency_value[option - 1], currency[option - 1])
                              print("Currency set to", client.get_currency())
                              print("Account balance:", "%0.2f" % client.get_account_balance(), client.get_currency())
                              input("\nPress Enter to continue ")
                              clear()

                        elif option == 0:  #back
                          break

                    elif option == 2:  #change data
                      validate = 0
                      while validate == 0:
                        print("Name:", client.get_client_name(), "\nID:", client.get_id(), "\nPassword:", client.get_password())
                        option = input("1. Change name\n2. Change id\n3. Change password\n\n0. Back\n")
                        validate = validate_choice(option, 0, 3)
                      option = int(option)
                      clear()

                      while True:
                        if option == 1:  #change name
                          new_name = input("Enter new name: ")
                          client.set_client_name(new_name)
                          clear()
                          print("Name set to", client.get_client_name())
                          input("\nPress Enter to continue ")
                          clear()

                        if option == 2:  #change id
                          check_id = 0
                          while check_id == 0 or check_id == 1:
                            check_id = 0
                            new_id = input("Clients id: ")
                            for client in client_list:
                              if new_id == client.get_id():
                                print("ID already exists")
                                check_id = 1
                            if check_id == 0:
                              break
                          client.set_id(new_id)
                          clear()
                          print("ID set to", client.get_id())
                          input("\nPress Enter to continue ")
                          clear()

                        if option == 3:  #change password
                          while True:
                            new_pass = input("Password: ")
                            if len(new_pass) <= 3:
                              print("Password must be longer than 3 symbols")
                            else: 
                              break
                          client.set_password(new_pass)
                          clear()
                          print("Password set to", client.get_password())
                          input("\nPress Enter to continue ")
                          clear()

                        if option == 0:  #back
                          break
                    elif option == 0:
                      back = 0
                      break

                else:  #wrong password
                  client.add_password_try()
                  clear()
                  print("Wrong password")
                  if client.get_password_tries() == 3:
                    print("Account blocked")
                    input("\nPress Enter to continue ")
                    clear()
                  else:
                    print(3 - client.get_password_tries(), "try/tries left\n")

            not_found = 0

        if not_found == 1:
          print("Wrong ID\n")

  elif option == 0:  #exit
    print("Program closed")
    break