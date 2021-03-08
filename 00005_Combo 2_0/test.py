
  def test_anterior1_es_0(self):
    self.assertEqual(anterior(1), 0);

  def test_anterior_10_es_9(self):
    self.assertEqual(anterior(10), 9)

  def test_triple_1_es_3(self):
    self.assertEqual(triple(1), 3)

  def test_triple_3_es_9(self):
    self.assertEqual(triple(3), 9)

  def test_anterior_del_triple_1_es_2(self):
    self.assertEqual(anterior_del_triple(1), 2)

  def test_anterior_del_triple_3_es_8(self):
    self.assertEqual(anterior_del_triple(3), 8)

  def test_anterior_del_triple_10_es_29(self):
    self.assertEqual(anterior_del_triple(10), 29)



