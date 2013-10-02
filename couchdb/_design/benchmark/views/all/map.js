function(doc) {
  if (doc.doc_type == "Benchmark")
    emit(doc.key, doc.content);
}
