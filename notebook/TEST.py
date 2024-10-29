# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
def factorial(n):
    """Computes factorial of n.
    
    Arguments:
    n -- nonnegative integer


   """
    if not isinstance(n, int) or n < 0:
        raise ValueError('Value of n should be nonnegative integer')
        
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
    


# %%
n = 5
list(range (1, n+1))


# %%
factorial(7)

# %%
