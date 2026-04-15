"""
পাইথনে প্রতিটি value একটি object এবং variable-গুলো হলো সেই অবজেক্টের দিকে নির্দেশকারী name বা reference।

1. Immutable Object
Immutable object তৈরির পর সেটির value বা state মেমোরিতে সরাসরি পরিবর্তন করা সম্ভব নয়। যদি কোনো operation বা command দিয়ে
value পরিবর্তন করার চেষ্টা করা হয়, তবে পাইথন একটি নতুন object তৈরি করে এবং variable-টিকে সেই নতুন অবজেক্টের দিকে নির্দেশ করে।
old object-টি অপরিবর্তিত থাকে।

# built-in Immutable Type:
- Numbers: int, float, complex
- Strings: str
- Booleans: bool
- Sequences: tuple, frozenset
- Special: NoneType (None)
"""

# পাইথনের id() function একটি object-এর unique memory address প্রদান করে।
x = 10
print("Immutable Object : ", id(x))  # address: 4328663984
x = x + 5     # এটি একটি নতুন object '15' তৈরি করে
print("Immutable Object : ", id(x))  # address: 4328664144

"""
এখানে x = x + 5 করার পর আগের 10 object-টি মেমোরিতে থেকে যায় যতক্ষণ না garbage collector সেটি delete করে, আর x নতুন 
একটি ১৫ ভ্যালুর object-কে point করে।
"""

"""
2. Mutable object
Mutable অবজেক্টের value বা state মেমোরিতে In-place পরিবর্তন করা সম্ভব। memory address বা object-এর id পরিবর্তন না করেই এর 
element add or modify করা যায়।

build-in Mutable type:
- Collections: list, dict, set
- Binary: bytearray
- Custom: বেশিরভাগ user-define class (যদি বিশেষভাবে ফ্রোজেন না করা হয়)।
"""

lst = [1, 2, 3]
print("Mutable Object : ", id(lst))     # address : 4300502848
lst.append(4)
print("Mutable Object : ", id(lst))     # address : 4300502848


"""
-> Immutable Object are Important : 
1. Performance & Memory
Immutable object গুলো পাইথন অনেক সময় cache (Interning) করে রাখে। যেমন: -৫ থেকে ২৫৬ পর্যন্ত ছোট integer গুলো মেমোরিতে একবারই তৈরি 
হয়। এটি মেমোরি সাশ্রয় করে এবং তুলনা করার গতি বাড়ায়। Mutable অবজেক্টের ক্ষেত্রে এমন caching স্বয়ংক্রিয়ভাবে হয় না।

2. Hashability
dictionary (dict) এর কি (Key) হিসেবে বা সেটের (set) উপাদান হিসেবে শুধুমাত্র Immutable Object ব্যবহার করা যায়। কারণ এদের hash value 
কখনো পরিবর্তন হয় না। Mutable অবজেক্টের ভ্যালু পরিবর্তনশীল হওয়ায় এদের hash value stable থাকে না, যা ডিকশনারি loopups নষ্ট করে দেয়।

3. Thread Safety
Immutable object গুলো thread safe, কারণ একাধিক thread একই সাথে data access করলেও data পরিবর্তনের ভয় থাকে না। ফাংশনে argument 
হিসেবে পাঠানোর সময় Immutable data মূল অবজেক্টের কোনো ক্ষতি করে না, কিন্তু Mutable data side-effect তৈরি করতে পারে।
"""

"""
-> The Tuple Exception: Objects within Objects
Tuple নিজে Immutable হলেও এর ভেতরে যদি কোনো Mutable object (যেমন: list) থাকে, তবে সেই list-এর ভেতরের element পরিবর্তন করা যায়।

টাপলের Immutability মানে:
- টাপলের element বদলানো যায় না (t[0] = new_value → TypeError)
- new element add/delete করা যায় না
- টাপলের নিজের id(t) এবং length কখনো বদলায় না

কিন্তু যদি টাপলের ভিতরে কোনো mutable (list, dictiory, set ইত্যাদি) থাকে, তাহলে সেই অভ্যন্তরীণ object-কে পরিবর্তন করা যায়। টাপল শুধু সেই 
অবজেক্টের reference ধরে রাখে — রেফারেন্সটা বদলায় না, কিন্তু ভিতরের মান বদলায়।
"""

t = (1, [2, 3])
print("Tuple Id : ", id(t))
print("Inside Tuple List Id : ", id(t[1]))  # address 4344596736
print("Tuple : ", t),

t[1].append(4)
print("After Modify Tuple Id : ", id(t))
print("After Modify Inside List Id : ", id(t[1]))  # address 4344596736
print("After Modify Tuple : ", t)

"""
Tuple যখন তৈরি করা হয়, তখন এটি সরাসরি ডেটা (যেমন: ১, ২, ৩) নিজের ভেতর জমা রাখে না। বরং এটি মেমোরিতে থাকা অন্য অবজেক্টগুলোর মেমোরি 
address বা pointer ধারণ করে।
- টাপলের index 0-তে আছে পূর্ণসংখ্যা 1 এর address।
- টাপলের index 1-তে আছে list [2, 3] এর addresss (4344596736)।

Tuple Immutable হওয়ার অর্থ হলো, টাপল তার ইনডেক্সগুলোতে যে address-গুলো ধরে রেখেছে, সেই address-গুলো সে কখনো পরিবর্তন করতে দেবে না। 
যেহেতু এখানে লিস্টের memory address-টি টাপলের solt থেকে সরিয়ে নতুন কোনো address বসানো হয়নি, তাই টাপলের নিজস্ব আইডি (4346201664) 
অপরিবর্তিত রয়ে গেছে।
"""
