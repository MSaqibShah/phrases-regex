affirmative_words = date_patterns = ['\\d{2} [a-zA-Z]{3}, \\d{4}', '\\d{2} [a-zA-Z]{3} \\d{4}', '\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2}', '[a-zA-Z]+, \\d{2} [a-zA-Z]+ \\d{4}', '\\d{2}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2}', '\\d{2}-\\d{2}-\\d{4} \\d{6}', '\\d{4}-\\d{2}-\\d{2}', '[a-zA-Z]+ \\d{2}, \\d{4}', '\\d{6}', '\\d{14}', '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}', '[a-zA-Z]+, \\d{2} [a-zA-Z]+ \\d{4} \\d{2}:\\d{2}:\\d{2}', '[a-zA-Z]+ \\d{2} \\d{4} \\d{2}:\\d{2}:\\d{2}', '\\d{4}/\\d{2}/\\d{2}', '[a-zA-Z]+ \\d{2}, \\d{4} \\d{2}:\\d{2}:\\d{2}',
                                     '[a-zA-Z]{3} \\d{2} \\d{4}', '\\d{2} [a-zA-Z]+, \\d{4}', '\\d{6} \\d{2}:\\d{2}:\\d{2}', '\\d{8}', '\\d{2} [a-zA-Z]+ \\d{4} \\d{6}', '\\d{2}/\\d{2}/\\d{2}', '\\d{2}-\\d{2}-\\d{2}', '\\d{2}/\\d{2}/\\d{4}', '\\d{4}/\\d{2}/\\d{2} \\d{2}:\\d{2}:\\d{2}', '\\d{2}-\\d{2}-\\d{4}', '[a-zA-Z]+ \\d{2} \\d{4}', '[a-zA-Z]+ \\d{2} [a-zA-Z]+ \\d{4} \\d{6}', '\\d{2} [a-zA-Z]+, \\d{4} \\d{2}:\\d{2}:\\d{2}', '[a-zA-Z]{3} \\d{2}, \\d{4}', '\\d{8} \\d{2}:\\d{2}:\\d{2}', '\\d{12}', '\\d{2} [a-zA-Z]+ \\d{4}', '\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2}']


print(len(affirmative_words))


def remove_duplicates(lst):
    return list(set(lst))


print(len(remove_duplicates(affirmative_words)))
print(remove_duplicates(affirmative_words))