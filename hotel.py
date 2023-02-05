import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        #Create Block
        self.blocks = [] 

        # Create Genesis block
        genesis = self.genesis_block = Block(index=len(self.blocks), data='Genesis Block',prev_hash='0')
        self.blocks.append(genesis)
        
    # Create block 
    def add_block(self, data):
        index = len(self.blocks)
        prev_hash = self.blocks[-1].hash
        block = Block(index, data, prev_hash)

        self.blocks.append(block)
    def select_hotel(self):
        hotel = Hotel('Great Eastern Hotel', 'London, EC2', 'Open', '1975', '15','256', 'Hyatt Hotels Corporation')
        hotel_b = Hotel('Ansonia Hotel', '2101,Broadway, New York, New York', 'Open', '1972', '12','222', 'Helen Godman')
        hotel_c= Hotel('The Chatwal New York', '128–132 West 44th Street, Manhattan, New York', 'Open', '1973', '13','231', 'Henry James Montague')
        hotel_d = Hotel('Webster Hotel', '40 West 45th Street, New York, New York', 'Open', '1975', '15','256', 'Hyatt Hotels Corporation')
        hotel_e = Hotel('Plaza Hotel', '768 Fifth Avenue, Manhattan, New York', 'Open', '1907', '21','195', 'Thomas Hastings')

        #Hotels Catagory
        print("1. Great Eastern Hotel")
        print("2. Ansonia Hotel")
        print("3. The Chatwal New York")
        print("4. Webster Hotel")
        print("5. Plaza Hotel")
        option = int(input("Select Hotel: "))
        buyer = input("Enter a New Hotel Owner: ")

        while True:
            if option == 1:
                hotel.buy_hotel(buyer)
                break
            elif option == 2:
                hotel_b.buy_hotel(buyer)
                break
            elif option == 3:
                hotel_c.buy_hotel(buyer)
                break
            elif option == 4:
                hotel_d.buy_hotel(buyer)
                break
            elif option == 5:
                hotel_e.buy_hotel(buyer)
                break
            else:
                print("Out of scope")
                continue

    def list_hotels(self):
        for block in self.blocks:
            print('\n--------------------Block Details--------------------')
            print(f'Block Index: {block.index}')
            print(f'Blocks Hash: {block.hash}')
            print(f'Previous Hash: {block.prev_hash}')
            print(f'Timestamp: {block.timestamp}')
            print('\n--------------------Hotel Details--------------------')
            print(f'{block.data}')
        


    def hotels_display(self, idx):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                print('\n--------------------Block Details--------------------')
                print(f'Block Index: {idx}')
                print(f'Blocks Hash: {block.hash}')
                print(f'Previous Hash: {block.prev_hash}')
                print(f'Timestamp: {block.timestamp}')
                print('\n--------------------Hotel Details--------------------')
                print(f'Data : {block.data}')
                
                
    def hotel_edit(self, idx, new_owner):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                block.data['new_hotel_owner: '] = new_owner
                block.hash = block.compute_hash()       

    def validate(self):
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if current_block.prev_hash != previous_block.hash:
                return "Data Change Detected !!"
        return "No data was changed."

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        
        self.hash = self.compute_hash()

    def compute_hash(self):
        tx = json.dumps(self.data)
        block_contents = (str(tx) + str(self.prev_hash)).encode()
        return hashlib.sha256(block_contents).hexdigest()
        
class Hotel:
    def __init__(self,hotel_name, hotel_location, hotel_status, hotel_built, hotel_floor_count, hotel_number_of_rooms, hotel_owner):
        
        self.hotel_name = hotel_name
        self.hotel_location = hotel_location
        self.hotel_status = hotel_status
        self.hotel_built = hotel_built
        self.hotel_floor_count = hotel_floor_count
        self.hotel_number_of_rooms = hotel_number_of_rooms
        self.owner = hotel_owner

    # Buy a Hotels
    def buy_hotel(self, buyer):
        self.owner = buyer
        transactions = {
            'hotel_name': self.hotel_name,
            'hotel_location': self.hotel_location,
            'hotel_status': self.hotel_status,
            'hotel_bilt': self.hotel_built,
            'hotel_floor_count': self.hotel_floor_count,
            'hotel_number_of_rooms': self.hotel_number_of_rooms,
            'hotel_owner': self.owner,
        }
        blockchain.add_block(transactions)

blockchain = Blockchain()

while True:
    print('-----------------------------------------------------')
    print('Start Program')
    print('Option 1: Buy a Hotel')
    print('Option 2: Show Hotel')
    print('Option 3: List Hotels')
    print('Option 4: Edit Hotels')
    print('Option 5: Modify Check')
    print('Option 6: Exit')
    print('-----------------------------------------------------')

    option = int(input("Option: "))
    match option:
        case 1:
                hotel_name = blockchain.select_hotel()
                print(hotel_name)
        case 2:
                block_index = int(input("Enter Block Index To Shows: "))
                blockchain.hotels_display(block_index) 
        case 3:
                blockchain.list_hotels()
        case 4:
                block_index = int(input("Enter Block Index To Edit: "))
                owner = input("Owner: ")
                blockchain.hotel_edit(block_index, owner)
        case 5:
                valid = blockchain.validate()
                print(valid)
        case 6:
                break
        case _:
                print('You entered the wrong number!!!')
