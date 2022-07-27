#remove all the ladder steps 
rm stdErr/test_1/*
for n in {1..20};
do
	python3 randGraph.py > input/lad$n.txt $n
	echo "n : $n"
	echo "none naive running"
	python3 main_non.py < input/lad$n.txt > stdOut/main_non.txt 2>> stdErr/test_1/main_non.txt
	echo "inc semi-naive running with no del"
	python3 semi_incNoD.py < input/lad$n.txt > stdOut/semi_incNoD.txt 2>> stdErr/test_1/semi_incNoD.txt
	echo "inc semi-naive running"
	python3 semi_incD.py < input/lad$n.txt > stdOut/semi_incD.txt 2>> stdErr/test_1/semi_incD.txt
	echo "inc naive running"
	python3 naive_incD.py < input/lad$n.txt > stdOut/naive_incD.txt 2>> stdErr/test_1/naive_incD.txt
	echo $(diff -s stdOut/semi_incNoD.txt stdOut/semi_incD.txt)
	echo $(diff -s stdOut/semi_incD.txt stdOut/naive_incD.txt)
	echo $(diff -s stdOut/main_non.txt stdOut/semi_incD.txt)
done
