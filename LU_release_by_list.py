import list_of_list_with_lu_generator as generator

queue_string = "WAN-033867	WAN-029832	WAN-034128	WAN-029687	WAN-034060	WAN-031928	WAN-030843	WAN-028238	WAN-032984	WAN-033771	WAN-028985	WAN-028209	WAN-030054	WAN-034735	WAN-029951	WAN-029493	WAN-028942	WAN-033392	WAN-029956	WAN-031930	WAN-033927	WAN-028328	WAN-028850	WAN-031694	WAN-035151	WAN-035125	WAN-033141	WAN-034981	WAN-030739	WAN-032978	WAN-031999"
queue_list = queue_string.split()
queue_list_compare = queue_list.copy()
batch = generator.create_sorted_list_of_lists_containing_lu_by_orders()

batch2 = batch.copy()
queue = []

open_orders = set()
update_open_orders = set
count_open_orders = 0
orders_amount_on_begin = len(batch)


def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def order_list_by_length(batch_list):
    return sorted(batch_list, key=len)


def add_queue_item():
    queue.append(queue_list[0])
    queue_list.pop(0)


def delete_lu_from_lists(batch_list, item_to_delete):
    return [[item for item in sublist if item != item_to_delete] for sublist in batch_list]


orders_left = orders_amount_on_begin - len(batch)


print("lu on sorter | opened orders at all | orders ready to pack | opened orders not ready to pack")
while len(batch) > 0:
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch), len(open_orders) - orders_amount_on_begin + len(batch))
    # print(queue)
    # print(queue_list)
    add_queue_item()




    update_open_orders = get_indicates_of_order_containing_lu(batch2, queue[-1])
    open_orders = open_orders.union(update_open_orders)
    batch = delete_lu_from_lists(batch, queue[-1])
    batch = [sublist for sublist in batch if sublist]  # remove empty lists
    batch = order_list_by_length(batch)
if len(batch) == 0:
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch),
          len(open_orders) - orders_amount_on_begin + len(batch))
    print(queue)
    print(queue_list)


    # print(batch)
