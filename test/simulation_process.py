video = [0, 30]
clip = [(3, 5), (10, 16)]
in_p = [3, 10]
out_p = [5, 16]

offset1 = [3, 4, 5]
offset2 = [6, 7, 8, 9]
offset3 = [10, 11, 12]
offset4 = [13, 14]
offset5 = [15, 16]
offset6 = [17]
offset7 = [18, 19]

tasks = [offset1, offset2, offset3, offset4, offset5, offset6, offset7]
# offset按照顺序返回

# cur_in = None
# cur_out = None
task_num = 0  # 任务从切片1开始，0表示不在切片范围内

container = []

for offset_list in tasks:
    print(f"-----------{offset_list}-----------")
    if offset_list[0] in in_p:
        cur_in = offset_list[0]
        task_num = in_p.index(cur_in) + 1
        print(f"task_num:{task_num}, in:{cur_in}-{offset_list}-任务开始")

    if task_num > 0:

        if offset_list[-1] in out_p:
            cur_out = offset_list[-1]
            container.append(offset_list)
            print(f"task_num:{task_num}, 停止状态, container add: {offset_list}, clip: {in_p[task_num-1]}-{out_p[task_num-1]}")
            print(f"task_num:{task_num}, out:{cur_out}-{offset_list}-任务结束")
            print(f"{task_num} - container: {container}")
            task_num = 0
            # return container res
            container.clear()
        else:
            print(f"task_num:{task_num}, 区间状态, container add: {offset_list}, clip: {in_p[task_num-1]}-{out_p[task_num-1]}")
            container.append(offset_list)

    print("---------------------------------\n\n")
