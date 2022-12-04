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
                
        # nned to work on the sell side buy side is done
        
            
    def myfunc(self):
        return self.sell

     
        
        


            