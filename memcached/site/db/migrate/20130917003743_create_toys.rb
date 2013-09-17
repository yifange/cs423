class CreateToys < ActiveRecord::Migration
  def change
    create_table :toys do |t|
      t.string :key
      t.text :value

      t.timestamps
    end
    add_index :toys, :key
  end
end
