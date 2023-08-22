import sys


# python filename arg1, arg2 --> ['argv_ex.py', '0.3,0.9']
# args = sys.argv
# print(args)


#will check whether values has been given if not then take default one
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

print(alpha,l1_ratio)
