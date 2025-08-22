for file in *_words.txt; do
    # Count total tokens (lines in the file)
    total_tokens=$(wc -l < "$file")
    
    # Count unique types (unique words)
    unique_types=$(sort "$file" | uniq | wc -l)
    
    # calculating TTR
    ttr=$(echo "scale=4; $unique_types / $total_tokens" | bc)
    
    # printing the result
    echo "Genre: ${file%_words.txt}, Type-Token Ratio: $ttr"
done