def get_sequences(file,minsup):
    raw = open(file).read().split()
    raw = raw[1::2]
    val=[]
    for i in raw:
      val.append(i[1:len(i)-1])

    def count_sub(transaction):
        freq = {} 
        candidate = []
        for sub_len in range(1, len(transaction) + 1):
            for begin_index in range(0, len(transaction) - sub_len + 1):
                candidate.append(transaction[begin_index:begin_index+sub_len])
                for item in candidate: 
                    if (item not in freq): 
                        freq[item] = 1
        return freq

    globalcount={}
    for i in range(0,len(val)):
        subcount=count_sub(val[i])
        for k in subcount:
            if k in globalcount:
                globalcount[k] += subcount[k]
            else:
                globalcount[k] = subcount[k]

    result={k:v for (k,v) in globalcount.items() if v >= minsup}
    return result