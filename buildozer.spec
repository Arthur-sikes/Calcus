	def btn_action(self,_):
			self.filename = "barcode"
		     base_name = "barcode"
		     ext = '.png'
		     final_path = f'{base}_{self.suff}{ext}'
			barcode_type = self.btype.text.strip()
			serial = self.serial.text.strip()
			while os.path.exists(self.filename):
			     generate_barcode(barcode_type,serial,self.filename)
			     app.screenmanager.current = "show"
			else:
			      self.filename = "".join((self.filename,f"_{self.suff}"))
			      self.suff += 1
			      generate_barcode(barcode_type,serial,self.filename)
			      app.screenmanager.current = "show"