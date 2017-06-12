require 'csv'
# ruby btgen.rb formats/formats_progressive.txt bt_progressive.sh

# Create flag for I or P

module BT
  class Generate
    def initialize(file, generator)
      @file = file
      @generator = generator
    end

    def csv
      CSV.foreach(@file) do |r|
        system("sh #{@generator} #{r.join(' ')}")
      end
    end
  end
end

# @file = ARGV[0] || 'formats_progressive.txt'
# @generator = ARGV[1] || 'bt_progressive.sh'
generate = BT::Generate.new(ARGV[0], ARGV[1])

generate.csv
