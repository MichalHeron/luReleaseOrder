import list_of_list_with_lu_generator as generator


batch = generator.create_sorted_list_of_lists_containing_lu_by_orders()

batch2 = batch.copy()
queue = []

open_orders = set()
update_open_orders = set
count_open_orders = 0
orders_amount_on_begin = len(batch)
first_lu = "WAN-000000"
THE_LOWEST_AMOUNT_OF_OPENING_ORDERS = False #if true script pick this lu which belong to the lowest amount of orders in batch


def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def order_list_by_length(batch_list):
    return sorted(batch_list, key=len)


def add_queue_item(batch_list): #old version
    for i in batch_list[0]:
        queue.append(i)



def delete_lu_from_lists(batch_list, item_to_delete):
    return [[item for item in sublist if item != item_to_delete] for sublist in batch_list]


def next_lu_in_queue():
        min_list = [sublist for sublist in batch if len(sublist) == min(len(sublist) for sublist in batch)]

        lu_min_list = []
        lu_min_list_with_biggest_amount_of_open_orders = []
        lu_min_list_with_max_amount_of_belong_to_open_orders = []
        lu_min_list_with_max_amount_of_not_belong_to_open_orders = []
        lu_batch_list = []

        for list_lu in min_list:
            for lu in list_lu:
                lu_min_list.append(lu)
        lu_min_list_set = list(set(lu_min_list))
        for batch_lu in batch:
            for lu in batch_lu:
                lu_batch_list.append(lu)
        if THE_LOWEST_AMOUNT_OF_OPENING_ORDERS:
            count = 99999
        else:
            count = -1

        old_index_count = 0
        ne_lu = "empty"

        for lu in lu_min_list_set:    #checking whicht lu belong to the most or less amount of orders
            if count == lu_batch_list.count(lu):
               lu_min_list_with_biggest_amount_of_open_orders.append(lu)
            if THE_LOWEST_AMOUNT_OF_OPENING_ORDERS:
               if count > lu_batch_list.count(lu):
                    count = lu_batch_list.count(lu)
                    lu_min_list_with_biggest_amount_of_open_orders = [lu]
            else:
                if count < lu_batch_list.count(lu):
                   count = lu_batch_list.count(lu)
                   lu_min_list_with_biggest_amount_of_open_orders = [lu]


        for lu in lu_min_list_with_biggest_amount_of_open_orders: #checking from the last group which lu belong to a already opened oreders (has the most)
            new_index_count = 0
            lu_indicates = get_indicates_of_order_containing_lu(batch2, lu)
            for index in lu_indicates:
                if index in open_orders:
                    new_index_count += 1
            if new_index_count == old_index_count:
                lu_min_list_with_max_amount_of_belong_to_open_orders.append(lu)
            if new_index_count > old_index_count:
                lu_min_list_with_max_amount_of_belong_to_open_orders = [lu]
                old_index_count = new_index_count

        count_closed_orders = 0
        for lu in lu_min_list_with_max_amount_of_belong_to_open_orders: # if still has two or more will check wich one will close the most amount of orders
            if count_closed_orders < lu_min_list.count(lu):
                count_closed_orders = lu_min_list.count(lu)
                ne_lu = lu
            if count_closed_orders == lu_batch_list.count(lu): #additionall condition to keep consistency - just pick this one with the lowest number in name
                if lu < ne_lu:
                    ne_lu = lu

        return ne_lu


orders_left = orders_amount_on_begin - len(batch)


print("lu on sorter | opened orders at all | orders ready to pack | opened orders not ready to pack")
while len(batch) > 0:
    # print("@@@@@@@@@@@@@@@@@@@")
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch), len(open_orders) - orders_amount_on_begin + len(batch))
    next_lu = next_lu_in_queue()
    queue.append(next_lu)

    update_open_orders = get_indicates_of_order_containing_lu(batch2, next_lu)
    open_orders = open_orders.union(update_open_orders)
    batch = delete_lu_from_lists(batch, next_lu)

    batch = [sublist for sublist in batch if sublist]  # remove empty lists
    batch = order_list_by_length(batch)
if len(batch) == 0:
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch),
          len(open_orders) - orders_amount_on_begin + len(batch))
    print(queue)
    # print(batch)
