#remove and re add the last only edge of the ladder multiple times
rm stdErr/test_2/*
for n in {1..20};
do
	python3 randGraph_2.py > input/lad${n}_2.txt $n
	echo "n : $n"
	echo "inc semi-naive running with no del"
	python3 semi_incNoD.py < input/lad${n}_2.txt > stdOut/semi_incNoD_2.txt 2>> stdErr/test_2/2_semi_incNoD.txt
	echo "inc semi-naive running"
	python3 semi_incD.py < input/lad${n}_2.txt > stdOut/semi_incD_2.txt 2>> stdErr/test_2/2_semi_incD.txt
	echo "inc naive running"
	python3 naive_incD.py < input/lad${n}_2.txt > stdOut/naive_incD_2.txt 2>> stdErr/test_2/2_naive_incD.txt
	echo "none naive running"
	python3 main_non.py < input/lad${n}_2.txt > stdOut/main_non_2.txt 2>> stdErr/test_2/2_main_non.txt
	echo $(diff -s stdOut/semi_incNoD_2.txt stdOut/semi_incD_2.txt)
	echo $(diff -s stdOut/semi_incD_2.txt stdOut/naive_incD_2.txt)
	echo $(diff -s stdOut/main_non_2.txt stdOut/semi_incD_2.txt)
done
