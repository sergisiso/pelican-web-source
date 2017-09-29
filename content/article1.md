Title: Test Post
Date: 2010-12-03 10:20
Tags: programming, hpc
Status: draft


# Test post.
## Just testing some features.


Some style samples:
Tables
<table class="table table-striped">
<thead>
<tr>
<th>Tables</th>
<th align="center">Are</th>
<th align="right">Cool</th>
</tr>
</thead>
<tbody>
<tr>
<td>col 3 is</td>
<td align="center">right-aligned</td>
<td align="right">$1600</td>
</tr>
<tr>
<td>col 2 is</td>
<td align="center">centered</td>
<td align="right">$12</td>
</tr>
<tr>
<td>zebra stripes</td>
<td align="center">are neat</td>
<td align="right">$1</td>
</tr>
</tbody>
</table>

Python code

```python
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

roll_again = raw_input("Roll the dices again?")
```

C++ Code
```C++
#include<iostream>

class example{
int var1, var2;
public:
void set_request(int a, int b);
int sum(){return (var1+var2);}
}class_obj;

void example::set_request(int a, int b)
{
    var1 = a;
    var2 = b;
}

int main(void)
{
    class_obj.set_request(1,4);
    std::cout<<"\n The sum is "<<class_obj.sum()<<"\n";

    return 0;
}
```

Quotes

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
