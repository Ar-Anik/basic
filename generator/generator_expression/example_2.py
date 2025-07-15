# combine multiple generator expressions (Lazy Pipelines):
lines = (line.strip() for line in open('./log.txt'))
errors = (line for line in lines if 'ERROR' in line)

for err in errors:
    print(err)

# or
def line_f():
    for line in open('./log.txt'):
        yield line.strip()

def errors_f():
    for line in line_f():
        if 'ERROR' in line:
            yield line

error = errors_f()
print(next(error))
