try:
    import gc_content
    have_gc = True
except TmportError as e:
    print(e)
    have_gc = False
finally:
    #Do whatever is necessary
    pass
seq = 'AGTAACTAACTACAACAGAGACAGCA'

if have_gc:
    print(gc_content.gc(seq))
else:
    print(seq.count('G') + seq.count('C'))
    
