class Test(unittest.TestCase):

  def test_las_11_no_son_la_hora_de_la_verdad(self):
    self.assertFalse(hora_de_la_verdad(11))

  def test_las_14_no_son_la_hora_de_la_verdad(self):
    self.assertFalse(hora_de_la_verdad(14))
    
  def test_las_12_son_la_hora_de_la_verdad(self):
    self.assertTrue(hora_de_la_verdad(12))


