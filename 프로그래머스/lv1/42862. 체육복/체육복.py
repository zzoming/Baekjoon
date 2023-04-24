def solution(n, lost, reserve):

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    _reserve.sort()
    
    for i in _reserve :
        f = i-1
        b = i+1
        
        if f in _lost :
            _lost.remove(f)
        elif b in _lost :
            _lost.remove(b)
    
    return n - len(_lost)