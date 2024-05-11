import logging


def check_request(request, symbols):
    for c in request:
        if c not in symbols:
            logging.warning(f'symbol {c} isnt available')
            return False
    return True


def only_letters_digits_dash(request):
    s = {'-'}
    s.update([chr(i) for i in range(ord('a'), ord('z') + 1)])
    s.update([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    s.update([chr(i) for i in range(ord('0'), ord('9') + 1)])
    return check_request(request, s)


def only_printed_chars(request):
    s = {'-', ' ', '\n', ',', '.', ';', ':'}
    s.update([chr(i) for i in range(ord('a'), ord('z') + 1)])
    s.update([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    s.update([chr(i) for i in range(ord('0'), ord('9') + 1)])
    return check_request(request, s)
