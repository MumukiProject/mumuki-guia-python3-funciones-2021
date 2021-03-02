
  def test_le_gusta_leer_25_es_verdadero(self):
    self.assertTrue(le_gusta_leer(25))
  
  def test_le_gusta_leer_80_es_verdadero(self):
    self.assertTrue(le_gusta_leer(80))
  
  def test_le_gusta_leer_1_es_falso(self):
    self.assertFalse(le_gusta_leer(1))
  
  def test_le_gusta_leer_15_es_falso(self):
    self.assertFalse(le_gusta_leer(15))
  
  
