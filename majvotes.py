cong={
        7:5,
        18:22,
        32:8,
        71:9,
        66:6

        }
bjp={
        7:8,
        18:12,
        32:18,
        71:9,
        66:2

`        }
valid_cong=0
valid1_bjp=0
for key in cong:
    if key >18:
        valid_cong= valid_cong + cong[key]
for key in bjp:
    if key >18:
        valid1_bjp = valid1_bjp +  bjp[key]

if (valid1_bjp>valid_cong):
    print("bjp is leading by ",(valid1_bjp-valid_cong))
else:
    print("congress id leading by",(valid_cong-valid1_bjp))
