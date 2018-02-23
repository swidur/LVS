("CREATE TABLE brands("
                    "brand_id INTEGER PRIMARY KEY,name TEXT NOT NULL")


("CREATE TABLE t_types(type_id INTEGER PRIMARY KEY NOT NULL,name text NOT NULL")



("CREATE TABLE storagespaces(storage_id INTEGER PRIMARY KEY, stillage TEXT NOT NULL,x INTEGER NOT NULL CHECK (x > 0),y INTEGER NOT NULL CHECK (y > 0)")
					
					
("CREATE TABLE wheel(wheel_id INTEGER PRIMARY KEY,width INTEGER NOT NULL CHECK(width > 0),height INTEGER NOT NULL CHECK(height > 0),inches DOUBLE NOT NULL CHECK(inches > 0),t_depth DOUBLE,t_type INTEGER NOT NULL,brand INTEGER NOT NULL,dot INTEGER NOT NULL,storage_space_id INTEGER NOT NULL")
