CREATE TABLE `tblVocab` (
	`vocab_id` INTEGER NOT NULL,
	`canonical_id` INTEGER NOT NULL,
	`vocabulary` TEXT NOT NULL,
	`part_of_speech` TEXT NOT NULL,
	`type` TEXT NOT NULL,
	`gender` TEXT NOT NULL,
	`language` TEXT NOT NULL,
	PRIMARY KEY (`vocab_id`)
)

CREATE TABLE `tblRoot` (
	`canonical_id` INTEGER NOT NULL,
	`root` TEXT NOT NULL,
	PRIMARY KEY (`canonical_id`)
)

CREATE TABLE `tblContext` (
	`context_id` INTEGER NOT NULL,
	`context` TEXT NOT NULL,
	PRIMARY KEY (`context_id`)
)

CREATE TABLE `tblTags` (
	`tag_id` INTEGER NOT NULL,
	`tag` TEXT NOT NULL,
	PRIMARY KEY (`tag_id`)
)

CREATE TABLE `tblRecall` (
	`recall_id` INTEGER NOT NULL,
	`vocab_id` INTEGER NOT NULL,
	`date` TEXT NOT NULL,
	PRIMARY KEY (`recall_id`)
)