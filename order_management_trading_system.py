import heapq
import re
class Exchange:
    
    def __init__(self):
        self.buy = []
        self.sell = []
        heapq.heapify(self.buy)
        heapq.heapify(self.sell)
        

        
    def handle_order(self, order:str):
        temp = re.findall(r'[0-9]+', order)
        temp = [int(x) for x in temp][::-1]
        if "buy" in order:
            return self.buyOrder(temp)
        else:
            return self.sellOrder(temp)
            
    def buyOrder(self, arr):
        res = []
        if not self.sell:
            arr.insert(1, len(self.buy)+1)
            heapq.heappush(self.buy, arr)
            return "No pending sell orders"
        else:
            potMatching = [ x for x in self.sell if x[0]<= arr[0] ] ## potential matches to be excuted
            potMatching.sort(key=lambda x:x[1])
            self.sell = [x for x in self.sell if x not in potMatching]
            if not potMatching:
                arr.insert(1, len(self.buy)+1)
                heapq.heappush(self.buy,arr)
                return "No Matches"
            else:
                ordersToFill = arr[1]
                while potMatching and ordersToFill > 0:
                    temp = potMatching.pop(0) 
                    if ordersToFill<temp[2]:
                        temp = [temp[0],temp[1], temp[2] - ordersToFill, temp[3]]
                        heapq.heappush(potMatching, temp)
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1],ordersToFill, temp[0])])
                        ordersToFill = 0
                    elif ordersToFill == temp[2]:
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1], ordersToFill, temp[0])])
                        ordersToFill = 0
                    else:
                        ordersToFill -= temp[2]
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1],temp[2], temp[0])])
                if ordersToFill > 0:
                    arr[1] = ordersToFill
                    arr.insert(1, len(self.buy) +1)
                    heapq.heappush(self.buy, arr)
                for x in potMatching:
                    heapq.heappush(self.sell, x)
        return res
                        
    ## need to test some cases on the sellOrder Function
                    
    def sellOrder(self,arr):
        res = []
        if not self.buy:
            arr.insert(1, len(self.sell)+1)
            heapq.heappush(self.sell, arr)
            return "No pending Orders"
        else:
            potMatching = [ x for x in self.buy if x[0]>=arr[0] ] ## potential matches to be excuted
            potMatching.sort(key=lambda x:x[1])
            self.buy = [x for x in self.buy if x not in potMatching]
            if not potMatching:
                arr.insert(1, len(self.sell)+1)
                heapq.heappush(self.sell,arr)
                return "No Matches"
            else:
                ordersToFill = arr[1]
                while potMatching and ordersToFill > 0:
                    temp = potMatching.pop(0) 
                    if ordersToFill<temp[2]:
                        temp = [temp[0],temp[1], temp[2] - ordersToFill, temp[3]]
                        heapq.heappush(potMatching, temp)
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1],ordersToFill, temp[0])])
                        ordersToFill = 0
                    elif ordersToFill == temp[2]:
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1], ordersToFill, temp[0])])
                        ordersToFill = 0
                    else:
                        ordersToFill -= temp[2]
                        res.append(["{},{},{},{}".format(arr[-1], temp[-1],temp[2], temp[0])])
                if ordersToFill > 0:
                    arr[1] = ordersToFill
                    arr.insert(1, len(self.sell) +1)
                    heapq.heappush(self.sell, arr)
                for x in potMatching:
                    heapq.heappush(self.buy, x)
        return res
                
        
        
Example:
    order1 = "101,buy,10, 8"  # input order: index0 = order id, index1 = action, index2= quantity, index3 = price .
    order2 = "102,buy, 12, 10"
    order3 = "103,sell, 10, 10"
    trade = Exchange()
    trade.handle_order(order1) # will return "no pending selling orders" since there is orders in the queue to be sold. Order will be added to the queue to
                               # executed when an order with "sell" action comes in if the prices satisfy the condition
    trade.handle_order(order2) # will return "no pending selling orders" since there is orders in the queue to be sold
    trade.handle_order(order3) # since there are two pending order to be executed with an opposite action, it will execute against the pending orders
                               # whose prices greater than or equal to the prices from the opposite action queue based on the order placement. FIFO
                               # since the price of the first order is less than the price of the current action,it will het skipped and the order is excuted
                               # against the second order.
                               # return value ["103, 10, 10"]
                               # buy queue after executing is self.buy = [[8, 1,10, 101], [10, 2, 2, 102]]
                               # sell queue is empty. 
        
            
    

     
        
        


            
