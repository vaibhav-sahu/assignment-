
import time
#generator
def read_log(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

#decorator
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # run the actual function
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper  

@time_it
def filter_errors(lines):
    #list comprehension
    return [line for line in lines if "ERROR" in line]
@time_it
def uni_lvl(logs):
    return {line.split(',')[1] for line in logs}
@time_it
def level_counts(logs):
    return {lvl: sum(1 for line in logs if lvl in line) for  lvl in ['INFO', 'ERROR', 'WARNING']}



file_path = 'D:\\VS code Programs\\pyhton\\adv\\server.log'
lines=list(read_log(file_path))
error_lines=filter_errors(lines)
print('errors')
for error in error_lines:
     print(error)

level=uni_lvl(lines)
print("\n Unique Log Levels:", level)

print("\n Log Level Counts using dict comprehension:", level_counts(lines))



