Run: python3 impl2.py  (writes impl2.txt, runs brute force n<=4 and known-term checks).
Method: X^8=I <=> (X-I)^8=0 over GF(2); count nilpotent N with N^8=0 via recursion on
kernel dimension / image (see docstring in impl2.py): no Jordan types or centralizers.
