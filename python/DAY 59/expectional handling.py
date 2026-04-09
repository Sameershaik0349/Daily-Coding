# exeptional handling////
'''to find error easily
 

try ---for risky code
     ----and logic on code 

'''


# errors

# exception handling

'''name
type error
value
file not
attrib
key'''

# 1.NAME ERROR
'''
name = "asdfgfhng"
print(pin) ---its called name error
'''

# 2.TYPE ERROr
'''s=10+"pyhton"
print(s) ---type error
''' 

"value error"

'''try ---for risky code
     ----and logic on code

     
exception--- 
        it is like else if the the try block had error this expection will run for not crashimg the code  
     
     
     '''


'''try:
    name="python"
    print(pin)
# except Exception as p:
#     print(p)     when if we dont know erroe

except NameError:
    print('name error') #---if we know the error

except ZeroDivisionError():
    print("zerodiverror") '''


# except AttributeError():#uses in objects and classes


# ==============degfault & expect=============

'''deafault

print("default error")
its must in last
'''




"Else"

'''try:
    print(10/2)
except Exception as k:
    print(k)
else:
    print("expception else")
finally:
    print("finally")
'''

try:
    print("outer try")
    try:
        print("inner try")
        print(10/0)
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print(":zerodiv error")
    except IndexError:
        print("index error")
    except:
        print("---default -----")
    else:
        print("inner else")
    finally:
        print("inner finaaly block")
except FileNotFoundError:
    print("outer filenotfounderror")
except ValueError:
        print("outer value error")
except TypeError:
    print("type error")
except AttributeError:
    print("outer default")

except:
    print("outer defaulty")

else:
    print("outer else")
finally:
    print("outer final")


    