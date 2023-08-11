from wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from controller.sk_mongo_controller.sk_mongo_controller import MongoController


mongo_wrapper = MongoWrapper()
mongo_controller = MongoController()
mongo_wrapper.set_mongo_controller(mongo_controller)


data = {'$table1' : [{'item' : 'apple'},{'item' : 'banana'}],'$table2' : [{'item' : 'apple', 'stock_in' : 100 , 'stock_out' : 90},{'item' : 'banana', 'stock_in' : 100 , 'stock_out' : 90}]}
mongo_wrapper.set_table_data(data, ['table1:x', 'table2:y'])
##mongo_wrapper.join()


mongo_wrapper.query(["select({'item' : x.item.collection + x.item , '_id' : 0})"])



##mongo_wrapper.query(["select({'item' : x.item.collection - x.item,'item' : x.item.collection - x.item })"])
##mongo_wrapper.query(["select({'item' : x.item,'stock' : y.stock_in.sum()-y.stcok_out.sum() })"])



