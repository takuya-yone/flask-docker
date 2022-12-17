echo "GET http://k8s-default-fastapia-ec363a3251-1789873693.ap-northeast-1.elb.amazonaws.com/pod" | vegeta attack -rate=500 -duration=20s >  result.bin
cat result.bin | vegeta plot > result_plot.html