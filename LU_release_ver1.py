import list_of_list_with_lu_generator as generator


batch = generator.create_sorted_list_of_lists_containing_lu_by_orders()

batch2 = batch.copy()
queue = []

open_orders = set()
update_open_orders = set
count_open_orders = 0
orders_amount_on_begin = len(batch)
first_lu_in_queue = True   # if True the logic is ON to pick first LU in different way
first_lu = "WAN-000000"


def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def order_list_by_length(batch_list):
    return sorted(batch_list, key=len)


def add_queue_item(batch_list):
    for i in batch_list[0]:
        queue.append(i)


def delete_lu_from_lists(batch_list, item_to_delete):
    return [[item for item in sublist if item != item_to_delete] for sublist in batch_list]


orders_left = orders_amount_on_begin - len(batch)


print("lu on sorter | opened orders at all | orders ready to pack | opened orders not ready to pack")
while len(batch) > 0:
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch), len(open_orders) - orders_amount_on_begin + len(batch))

    if first_lu_in_queue:
        min_list = [sublist for sublist in batch if len(sublist) == min(len(sublist) for sublist in batch)]
        lu_min_list = []
        lu_batch_list = []
        for list_lu in min_list:
            for lu in list_lu:
                lu_min_list.append(lu)
        lu_min_list = list(set(lu_min_list))

        for batch_lu in batch:
            for lu in batch_lu:
                lu_batch_list.append(lu)

        count = len(set(lu_batch_list))
        for lu in lu_min_list:
            if count > lu_batch_list.count(lu):
                count = lu_batch_list.count(lu)
                first_lu = lu

        queue.append(first_lu)

    else:
        add_queue_item(batch)

    if first_lu_in_queue:
        update_open_orders = get_indicates_of_order_containing_lu(batch2, first_lu)
        open_orders = open_orders.union(update_open_orders)
        batch = delete_lu_from_lists(batch, first_lu)
        first_lu_in_queue = False
    else:
        for i in batch[0]:
            update_open_orders = get_indicates_of_order_containing_lu(batch2, i)
            open_orders = open_orders.union(update_open_orders)
            batch = delete_lu_from_lists(batch, i)

    batch = [sublist for sublist in batch if sublist]  # remove empty lists
    batch = order_list_by_length(batch)
if len(batch) == 0:
    print(len(queue), len(open_orders), orders_amount_on_begin - len(batch),
          len(open_orders) - orders_amount_on_begin + len(batch))
    print(queue)
    # print(batch)
