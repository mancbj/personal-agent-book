-- Keep a section's short introduction with the start of its table.
-- The Markdown and HTML remain free of print-only page-break instructions.
function Blocks(blocks)
  local result = pandoc.List()
  for i, block in ipairs(blocks) do
    if block.t == "Header" and block.level >= 2 then
      local text_length = 0
      for j = i + 1, math.min(i + 3, #blocks) do
        local following = blocks[j]
        if following.t == "Table" then
          result:insert(pandoc.RawBlock("latex", "\\Needspace{18\\baselineskip}"))
          break
        elseif following.t == "Para" then
          text_length = text_length + #pandoc.utils.stringify(following)
          if text_length > 600 then break end
        else
          break
        end
      end
    end
    result:insert(block)
  end
  return result
end
