# Order-Management-Trading-System
The trading system where orders are received as string with id number, action (buy/sell), quantity of stocks to be executed, and price to be executed at. If executed, matches are returned in the string format "id of the match, id of the submitted order, filled quantity, and the price at which order is filled. In the case of the partial matching,
same returning structure holds.
Utilized the priority queue structure to store the orders where the orders placed to be sold at lower prices are given first priority and matched with buying orders whose prices are greater than or equal to asking prices of selling orders. In the case where there are multiple matching, orders that are submitted first are executed first.
Same holds true for placing orders to buy stocks in which case it is matched with orders that are placed to be sold whose prices are less or or equal to the submitted price. After the match, if the quantity of the match is less than the current quantity 
of the placed order, the match is removed from the queue. If the quantity of the matched roder is greater than the quantity of the current order, the match is
put back in their respective queue with uodated available quantity.
