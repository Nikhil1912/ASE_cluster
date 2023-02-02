# HW 3 Script


### Document file for HW3 Main.py file



- To view all command line options run 
    ```python3 Main.py --help True ```

- To Run test cases 
    ```python3 Main.py```


```
Here are the list of options

OPTIONS:
  -d  --dump    on crash, dump stack   = False
  -f  --file    name of file           = ../etc/data/auto93.csv
  -F  --Far     distance to "faraway"  = .95
  -g  --go      start-up action        = data
  -h  --help    show help              = False
  -m  --min     stop clusters at N^min = .5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512

To run

python3 Main.py --seed 937162211

```
## Output
```
0 0 [8, 360, 215, 4615, 14, 70, 1, 10]
0 0.0 [8, 360, 215, 4615, 14, 70, 1, 10]
50 0.14 [8, 318, 150, 4237, 14.5, 73, 1, 10]
100 0.3 [6, 250, 100, 3336, 17, 74, 1, 20]
150 0.39 [6, 225, 100, 3630, 17.7, 77, 1, 20]
200 0.58 [4, 156, 105, 2745, 16.7, 78, 1, 20]
250 0.71 [4, 116, 90, 2123, 14, 71, 2, 30]
300 0.74 [4, 115, 95, 2694, 15, 75, 2, 20]
350 0.82 [4, 134, 90, 2711, 15.5, 80, 3, 30]
✅PASS : eg_around
✅PASS : eg_check_nums
✅PASS : eg_check_rands
✅PASS : eg_check_syms
✅PASS : eg_clone
398 {'Lbs-': 2970.4, 'Acc+': 15.6, 'Mpg+': 23.8}
| 200 
| | 101 
| | | 51 
| | | | 26 {'Lbs-': 4129.1, 'Acc+': 12.4, 'Mpg+': 12.3}
| | | | 25 {'Lbs-': 3769.8, 'Acc+': 14.1, 'Mpg+': 16.0}
| | | 50 
| | | | 26 {'Lbs-': 4266.1, 'Acc+': 12.2, 'Mpg+': 13.8}
| | | | 24 {'Lbs-': 2557.7, 'Acc+': 16.6, 'Mpg+': 22.1}
| | 99 
| | | 50 
| | | | 26 {'Lbs-': 3832.7, 'Acc+': 14.4, 'Mpg+': 17.7}
| | | | 24 {'Lbs-': 3428.2, 'Acc+': 17.4, 'Mpg+': 20.0}
| | | 49 
| | | | 25 {'Lbs-': 3721.2, 'Acc+': 15.0, 'Mpg+': 21.2}
| | | | 24 {'Lbs-': 2845.4, 'Acc+': 16.0, 'Mpg+': 23.3}
| 198 
| | 100 
| | | 51 
| | | | 26 {'Lbs-': 2332.9, 'Acc+': 15.6, 'Mpg+': 27.7}
| | | | 25 {'Lbs-': 2389.3, 'Acc+': 16.8, 'Mpg+': 25.6}
| | | 49 
| | | | 25 {'Lbs-': 2676.6, 'Acc+': 17.2, 'Mpg+': 30.8}
| | | | 24 {'Lbs-': 2592.9, 'Acc+': 17.0, 'Mpg+': 30.4}
| | 98 
| | | 50 
| | | | 26 {'Lbs-': 2035.2, 'Acc+': 17.2, 'Mpg+': 29.6}
| | | | 24 {'Lbs-': 2342.2, 'Acc+': 15.7, 'Mpg+': 25.4}
| | | 48 
| | | | 25 {'Lbs-': 2332.4, 'Acc+': 15.6, 'Mpg+': 32.0}
| | | | 23 {'Lbs-': 2091.7, 'Acc+': 16.4, 'Mpg+': 35.2}
✅PASS : eg_cluster
✅PASS : eg_csv
✅PASS : eg_data
200 198 398
[4, 97, 67, 2065, 17.8, 81, 3, 30] 0.7119546410829445
[4, 121, 113, 2234, 12.5, 70, 2, 30]
[6, 258, 110, 2962, 13.5, 71, 1, 20]
✅PASS : eg_half
398 {'Lbs-': 2970.4, 'Acc+': 15.6, 'Mpg+': 23.8}
| 200 
| | 101 
| | | 51 
| | | | 26 {'Lbs-': 2302.6, 'Acc+': 15.5, 'Mpg+': 27.7}
✅PASS : eg_optimize
y mid {'Lbs-': 2970.42, 'Acc+': 15.57, 'Mpg+': 23.84}
 div {'Lbs-': 846.84, 'Acc+': 2.76, 'Mpg+': 8.34}
x mid {'Clndrs': 5.45, 'Volume': 193.43, 'Model': 76.01, 'origin': 1}
 div {'Clndrs': 1.7, 'Volume': 104.27, 'Model': 3.7, 'origin': 1.3273558482394003}
✅PASS : eg_stats
{'dump': False, 'file': '../etc/data/auto93.csv', 'Far': 0.95, 'go': 'data', 'help': False, 'min': 0.5, 'p': 2, 'seed': 937162211, 'Sample': 512}
✅PASS : eg_the

```
