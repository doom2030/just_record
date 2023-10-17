
# python3.7 协程

# *********************************************************************
import asyncio
import random

async def factorial(name):
   print(f"task_name: {name} is begin")
   await asyncio.sleep(random.randint(1, 5))
   print(f"task_name: {name} is end")
   return name.lower()

async def main():
    # 创建多个协程任务
    await asyncio.gather(
        factorial("A"),
        factorial("B"),
        factorial("C"),
    )
    # tasks = [factorial(i) for i in ["A", "B", "C", "D"]]
    # await asyncio.gather(*tasks)

asyncio.run(main())

# *********************************************************************

import asyncio
import random

async def factorial(name):
   print(f"task_name: {name} is begin")
   await asyncio.sleep(random.randint(1, 5))
   print(f"task_name: {name} is end")
   return name.lower()

async def main():
    # 获取单个协程任务的返回结果
    tasks = [factorial(i) for i in ["A", "B", "C", "D"]]
    for coro in asyncio.as_completed(tasks):
        res = await coro
        print(f"任务结果: {res}")

asyncio.run(main())


import asyncio
import random

async def factorial(name):
   print(f"task_name: {name} is begin")
   await asyncio.sleep(random.randint(1, 5))
   print(f"task_name: {name} is end")
   return name.lower()

async def main():
    # 获取多个协程任务的返回结果
    tasks = [factorial(i) for i in ["A", "B", "C", "D"]]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())



import asyncio

async def say_hello():
    print("hello begin")
    await asyncio.sleep(1)
    print("hello end")

# 创建一个原生协程对象
say_hello = say_hello()
# 创建一个task对象(侧重任务处理过程)
task = asyncio.create_task(say_hello)
# 创建一个future对象(侧重任务处理后的结果)
future = asyncio.ensure_future(say_hello)

# 使用事件循环,执行单个协程，任务，future对象，直到任务完成
loop = asyncio.get_event_loop()
# 可以接受一个task对象
loop.run_until_complete(task)
# 可以接收一个future对象
loop.run_until_complete(future)
# 可以接受一个协程(coroutine)对象
loop.run_until_complete(say_hello)

# 使用事件循环执行多个协程，任务，future对象，直到任务完成
coroutines = [say_hello, say_hello, say_hello]
tasks = [asyncio.create_task(say_hello), asyncio.create_task(say_hello), asyncio.create_task(say_hello)]
futures =  [asyncio.ensure_future(say_hello), asyncio.ensure_future(say_hello), asyncio.ensure_future(say_hello)]
loop.run_until_complete(coroutines)
loop.run_until_complete(tasks)
loop.run_until_complete(futures)

# asyncio.gather()可以接收 协程对象，task对象，future对象 def gather(*coroutines_or_futures, loop=None, return_exceptions=False) 通过*args位置传参，传多个对象

# 可以通过三种形式获取协程结果
async def coro():
    return 'result'

# 使用三种方式获取相同结果, 返回的都是协程的结果,因为task和future都只是对协程做了一层封装而已
result1 = coro() # 没有result()方法
result2 = asyncio.create_task(coro()).result()
result3 = asyncio.ensure_future(coro()).result()

print(result1)  # result
print(result2)  # result  
print(result3)  # result


# 回调函数是在任务执行完成后，才会被调用默认第一个参数是任务本身, def callback(task, *args, **kwargs):  可以同*args和**kwargs传入其他参数
# 回调函数执行情况：1. 任务成功完成时,返回结果。回调函数被调用,传入任务对象。2. 任务遇到异常结束时。回调函数被调用,传入任务对象。3. 任务被取消时。回调函数被调用,传入任务对象。
async def do_some_work(x):
    print(f'Working on {x}...')
    await asyncio.sleep(3)
    return f'{x} result' 

task1 = do_some_work(1) 
task2 = do_some_work(2)

def callback(task):
    print(f'Callback for {task} called')
    result = task.result()
    print(f'Result: {result}')

task1.add_done_callback(callback)
task2.add_done_callback(callback)

asyncio.gather(task1, task2)


# 完整示例
async def coro():
    pass

task = asyncio.create_task(coro())   

def callback(task):
    print('Callback called')
task.add_done_callback(callback)  

loop = asyncio.get_event_loop()  
loop.run_until_complete(task)

# 回调函数的使用示例
def callback(task):
    # 任务状态1被取消
    if task.cancelled():
        print('Task cancelled')
    # 任务状态2 异常
    elif task.exception():
        print(f'Task exception: {task.exception()}') 
    else:
        # 任务状态3 成功
        result = task.result()
        print(f'Task result: {result}')

# 通过task.exception()获取错误信息, traceback可以打印具体的错误栈信息
import traceback
def callback(task):
    exc = task.exception()
    print(f'Task exception: {exc}')  # 仅打印异常类型
    traceback.print_tb(exc.__traceback__)  # 打印详细调用栈



# 定义一个协程
async def print_info():
    print("hello")
    await asyncio.sleep(5)
    print("world")

# 创建协程
# 原生协程
coro = print_info()
# task包装
task = asyncio.create_task(print_info())
# future包装
future = asyncio.ensure_future(print_info())

# 获取协程结果
# print(coro.result()) # 错误,原生协程并没有result()的方法  只能是print(coro)获取协程的return结果
print(task.result())
print(future.result())

# 定义一个回调函数(只有下面三种情况, 回调函数才会触发)
def test_call_back(c):
    # 被取消
    if c.cancled():
        pass
    # 执行异常
    elif c.exception():
        pass
    # 执行成功
    else:
        print(c.result())

# 为协程添加回调函数
# coro.add_done_callback(test_call_back) # 错误，原生协程并不能添加回调函数，只能执行内部逻辑
task.add_done_callback(test_call_back)
future.add_done_callback(test_call_back)

# 运行协程方式有几种(方式一：asyncio.gather())
# asyncio.gather(coro) # 错误，asyncio.gather()只能运行task和future对象,不能运行原生协程对象
asyncio.gather(task)
asyncio.gather(future)

# 运行协程方式二，事件循环可以运行原生协程对象，task对象，future对象
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)
loop.run_until_complete(task)
loop.run_until_complete(future)


# 多个协程的创建，执行，获取结果
"""
asyncio.run()无法直接运行这些对象,因为:
- asyncio.run()会自动创建事件循环,并期望传入一个协程函数以转换为Task运行。
- 但是,你已经创建了coroutine对象、Task和Future,asyncio.run()无法直接识别这些对象来执行其操作。 
- 所以,我们需要手动获取事件循环,然后通过调用run_until_complete、add_done_callback或run_forever来执行这些异步对象。
总结来说,要运行coroutine对象、Task和Future,主要步骤是:
1. 获取事件循环
2. 通过调用run_until_complete、add_done_callback或run_forever执行对象
3. asyncio.run()只支持直接运行协程函数,更复杂的情况需要手动控制事件循环
"""

# 对于使用run_until_complete()运行的coroutine对象、Task和Future,可以这样获取其结果:
# 1. coroutine对象:
# 在协程函数中直接使用return返回结果,然后在run_until_complete()调用后的变量中获取:
async def coro():
    return 'result'

# 原生协程
result = loop.run_until_complete(coro())
print(result)  # result

# task
task = asyncio.create_task(coro())
loop.run_until_complete(task)
print(task.result()) # result

# task和future区别,一个是任务执行，一个是获取未来结果

# future
future = asyncio.ensure_future(coro())
loop.run_until_complete(future)
print(future.result()) # result


"""
要同时运行多个coroutine对象并获取结果,可以使用asyncio.gather()。
asyncio.gather()会将多个协程包装为Future对象,并将这些Future对象汇集为一个Future对象。然后你可以运行这个汇集的Future,并在其完成时获取每个协程的结果。
示例代码:
这里我们将3个coroutine对象封装为Future,然后使用asyncio.gather()汇集为一个Future对象futures。
在主协程main()中等待futures完成,然后从中获取每个协程的结果。
所以,要同时运行多个coroutine对象并获取结果,主要步骤是:
1. 创建多个coroutine对象
2. 使用asyncio.gather()将这些对象封装为Future并汇集为一个Future
3. 等待这个汇集的Future完成
4. 从 Future.result() 获取每个协程的结果
asyncio.gather()使我们可以很方便的并发运行多个协程,并从中获取结果
"""
import asyncio

async def coro1():
    return 'coro1'

async def coro2():
    return 'coro2'

async def coro3():
    return 'coro3'

async def main():
    coros = [coro1(), coro2(), coro3()]
    futures = asyncio.gather(*coros)
    
    result = await futures
    print(result)

asyncio.run(main())
# 输出: ['coro1', 'coro2', 'coro3']

"""
1. asyncio.gather()会并发运行多个协程,但返回一个总Future代表所有协程的完成。
2. 这个总Future只有当所有协程Future完成后才会自己完成。
3. 等待这个总Future会阻塞直到所有协程完成,才能获取结果。
4. 要避免阻塞,可以为这个总Future添加回调来获取结果。
5. gather()返回的结果列表顺序对应传入的协程,与协程的完成顺序无关。
希望这个详细的解释能够帮助你进一步理解asyncio.gather()的工作机制。如果你有其他问题,欢迎提出
如果你不想等待asyncio.gather()返回的Future完成(即所有协程完成)才获取结果,可以:
1. 为gather()返回的Future添加回调,在回调中处理每个协程完成后的结果。
2. 使用asyncio.as_completed()迭代gather()返回的Future,此方法会在每个Future完成时产生其结果,可以立即处理。
例如:
"""
import asyncio

async def coro1():
    await asyncio.sleep(2)
    return 'coro1'

async def coro2():
    await asyncio.sleep(1)
    return 'coro2'

async def coro3():
    await asyncio.sleep(3)
    return 'coro3'

async def main(): 
    coros = [coro1(), coro2(), coro3()]
    futures = asyncio.gather(*coros)

    # 方法1: 添加回调
    def result_callback(future):
        result = future.result()
        print(f'Get result: {result}')
        
    futures.add_done_callback(result_callback)
    
    # 方法2: 使用as_completed迭代
    for future in asyncio.as_completed(futures):
        result = await future
        print(f'Get result: {result}')

asyncio.run(main())



"""
要并发运行多个Task和Future对象并获取其结果,可以:
1. 使用asyncio.gather()并发运行这些对象,并等待其返回的Future获取结果:
"""
tasks = [asyncio.create_task(coro1()), asyncio.create_task(coro2())]
futures = [asyncio.ensure_future(coro1()), asyncio.ensure_future(coro2())]

results = await asyncio.gather(*tasks)     # 或 await asyncio.gather(*futures)
print(results)  # [coro1 result, coro2 result]

# 2. 使用asyncio.as_completed()迭代多个Task/Future对象,在完成时获取结果:
for task in asyncio.as_completed(tasks):
    result = await task
    print(result)

# 3. 添加回调到多个Task/Future对象,在回调中获取结果: 
def task_done(task):
    result = task.result()
    print(result)

for task in tasks:
    task.add_done_callback(task_done) 

# 4. 直接await每个Task/Future对象并获取结果:

for task in tasks:
    result = await task
    print(result)
"""
所以,总结来说,并发运行多个Task和Future对象并获取结果的方法有:
1. 使用asyncio.gather()并发运行,并在其返回的Future中获取所有结果。
2. 使用asyncio.as_completed()迭代,在完成时获取每个结果。
3. 为每个对象添加回调,在回调中获取结果。
4. 直接await每个对象获取结果(较低效)。
除gather()外的其他方法顺序取决于各对象的完成时间,gather()方法返回的结果列表顺序对应输入的对象,与完成顺序无关。
使用asyncio.gather()或asyncio.as_completed()都是高效的并发运行多个异步对象并获取结果的好方法。gather()更简单,但as_completed()提供更精细的控制。
"""

"""
可以使用事件循环的run_until_complete()方法并发运行多个异步对象。
- 要获取结果,可以在对象中return并从run_until_complete()调用获取、调用.result()方法或添加回调。
- 与gather()相比,使用run_until_complete()并发运行对象更加灵活,但获取结果较复杂,gather()提供一致的接口获取所有对象的结果。
- 两个方法都可以高效的并发运行异步对象,选择取决于结果获取和处理的需求
"""
import asyncio

async def coro1():
    await asyncio.sleep(2)
    return 'coro1'

async def coro2():
    await asyncio.sleep(1)
    return 'coro2'  

coro1 = coro1() 
coro2 = coro2() 
task1 = asyncio.create_task(coro1())
task2 = asyncio.create_task(coro2())

loop = asyncio.get_event_loop()
loop.run_until_complete(coro1)
loop.run_until_complete(coro2) 
loop.run_until_complete(task1)
loop.run_until_complete(task2)

# 1. 在对象中直接return,并从run_until_complete()调用中获取:
result1 = loop.run_until_complete(coro1)

# 2. 调用Task/Future的result()方法:
loop.run_until_complete(task1)
result1 = task1.result()

# 3. 为对象添加回调,在回调中获取结果:
def callback(task):
    result = task.result()
    print(result)

task1.add_done_callback(callback)
loop.run_until_complete(task1)
# 也可以添加多个
loop.run_until_complete(coro1, coro2, task1, task2)

# 获取结果1
results = loop.run_until_complete(coro1, coro2)
result1 = results[0]
result2 = results[1]
# 获取结果2
loop.run_until_complete(task1, task2)
result1 = task1.result() 
result2 = task2.result()
# 获取结果3
def callback(task):
    result = task.result()
    print(result)

task1.add_done_callback(callback)
task2.add_done_callback(callback)
loop.run_until_complete(task1, task2)
"""
所以,run_until_complete()方法可以并发运行多个异步对象,并在所有对象完成后:
- 直接从其返回值中获取结果(对于coroutine对象)
- 调用对象的result()方法获取结果(对于Task和Future)
- 或者在回调中获取结果
与asyncio.gather()相比,run_until_complete()并发运行多个对象的方法更加灵活,但获取结果较为复杂。gather()提供一致的接口获取所有对象的结果。
两者都是高效并发运行异步对象的好方法,选择视情况而定。
"""