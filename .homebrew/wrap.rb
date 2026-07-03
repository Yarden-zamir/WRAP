# typed: false
# frozen_string_literal: true

class Wrap < Formula
  desc "Generates 'wraps' for functions in any language using 'processors'"
  homepage "https://github.com/Yarden-zamir/WRAP"
  url "{{URL}}"
  sha256 "{{SHA256}}"
  license "MIT"

  depends_on "python@3.11"

  def install
    libexec.install Dir["*"]
    bin.write_exec_script libexec/"wrap"
    (libexec/"VERSION").write version
  end

  def caveats
    <<~EOS
      To activate wrap, run the following command:
        wrap install
      You can also use
        wrap install --help
      for custom installation.
    EOS
  end
end
