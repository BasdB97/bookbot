def get_num_words(text):
  return len(text.split())
  
def get_chars_dict(text):
  counts = {}
  for ch in text.lower():
    if ch in counts:
      counts[ch] += 1
    else:
      counts[ch] = 1
  return counts

def sort_on(d):
  return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
  sorted_list = []
  for ch in num_chars_dict:
    sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list  