down = tuple(
    int(re.sub('[^v]', '0', line).replace('^', '1'), 2),
    for line in lines
)