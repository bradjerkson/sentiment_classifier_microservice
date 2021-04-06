a="I love the park!"

echo "Testing!\n"

echo "$a"
curl -H "Content-type: application/json" \
  --request POST \
  --data '{"text": "$a"}' \
  http://localhost:80/analysis


b="I am having an awful day!"
echo "$b"
curl -H "Content-type: application/json" \
    --request POST \
    --data '{"text": "$b"}' \
    http://localhost:80/analysis
