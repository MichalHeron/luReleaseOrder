import list_of_list_with_lu_generator as generator


batch = generator.create_sorted_list_of_lists_containing_lu_by_orders()
queue = []
set_of_open_orders = set()
count_open_orders = 0
orders_amount_on_begin = len(batch)
point = 0
add_point_for_not_belong_to_order = 1
minus_point_for_belong_to_order = 3
minus_extra_point_for_last_lu_in_order = 5
set_method_of_picking_first_lu = False  # if True the logic to pick is original if False is by list


def create_lu_list(batch):
    unique_set = set()
    for sublist in batch:
        unique_set.update(set(sublist))
    return unique_set


lu_list_set = create_lu_list(batch)
lu_set_length = len(lu_list_set)
lu_amount_on_begin = lu_set_length
print(lu_amount_on_begin)


def count_finished_orders():
    count = 0
    for i in batch:
        if len(i) < 1:
            count += 1
    return count


def get_lu_amount_of_order_containing_lu(main_list, target_value):
    return [len(sublist) for sublist in main_list if target_value in sublist]


def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def delete_lu_from_lists(batch_list, item_to_delete):
    new_batch = []
    for sublist in batch_list:
        new_sublist = [item for item in sublist if item != item_to_delete]
        new_batch.append(new_sublist)
    return new_batch
    # return [sublist for sublist in batch_list if item_to_delete not in sublist]


def first_lu_in_queue(batch, lu_list_set):
    first_lu_points = 100000
    first_lu = "WAN-000000"
    for lu in lu_list_set:
        lu_points = sum(get_lu_amount_of_order_containing_lu(batch, lu))
        if lu_points < first_lu_points:
            first_lu_points = lu_points
            first_lu = lu
    return first_lu


def first_lu_in_queue_by_list(batch_list):
    return batch_list[0][0]



def get_next_lu(): #generate next lu to queue - it searching LU which start the lowest amount of orders and which is part of started orders
    point = 10000
    lu_with_lowest_points = "WAN-000000"
    for lu in lu_list_set:
        new_point = 0
        order = 0
        for sublist in batch:
            if lu in sublist:
                if order not in set_of_open_orders:
                    new_point += add_point_for_not_belong_to_order
                if order in set_of_open_orders:
                    if len(sublist) < 2:
                        new_point -= minus_extra_point_for_last_lu_in_order
                        # print("extra minus point")
                    new_point -= minus_point_for_belong_to_order
            order += 1
        if new_point < point:
            point = new_point
            lu_with_lowest_points = lu
    return lu_with_lowest_points


if(set_method_of_picking_first_lu):
    set_of_open_orders = get_indicates_of_order_containing_lu(batch, first_lu_in_queue(batch, lu_list_set))
    queue.append(first_lu_in_queue(batch, lu_list_set))
if(not set_method_of_picking_first_lu):
    set_of_open_orders = get_indicates_of_order_containing_lu(batch, first_lu_in_queue_by_list(batch))
    queue.append(first_lu_in_queue_by_list(batch))


lu_amount_remaining = lu_set_length - 1
count_open_orders = len(set_of_open_orders)
firstString = "1 "
firstString += str(count_open_orders)
firstString += " "
batch = delete_lu_from_lists(batch, queue[-1])
lu_list_set.remove(queue[-1])
firstString += str(count_finished_orders())
firstString += " "
empty_lists = [sublist for sublist in batch if len(sublist) == 0]
firstString += str(count_open_orders - len(empty_lists))
print("lu on sorter | opened orders at all | orders ready to pack | opened orders not ready to pack")
print(empty_lists)
print("0 0 0 0")
print(firstString)

while orders_amount_on_begin - count_finished_orders() > 0:
    queue.append(get_next_lu())
    new_set_of_open_orders = get_indicates_of_order_containing_lu(batch, queue[-1])
    set_of_open_orders = set_of_open_orders.union(new_set_of_open_orders)
    count_open_orders = len(set_of_open_orders)
    batch = delete_lu_from_lists(batch, queue[-1])
    if lu_list_set:
        lu_list_set.remove(queue[-1])
    else:
        lu_list_set.remove(0)
    lu_set_length = len(lu_list_set)
    empty_lists = [sublist for sublist in batch if len(sublist) == 0]
    lu_amount_remaining = lu_set_length
    print(lu_amount_on_begin - lu_amount_remaining, count_open_orders, count_finished_orders(),
          count_open_orders - len(empty_lists))
print(queue)